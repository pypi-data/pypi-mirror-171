use std::collections::BTreeMap;

use super::{
    named_axes::get_axis_leaves, prelude::*, Index, ModuleNodeArgSpec, ModuleNodeSpec, Symbol,
};
use crate::circuit::Concat;
use crate::circuit::{deep_map_unwrap, named_axes::set_named_axes, CircResult, ModuleNode};
use crate::tensor_util::TensorAxisIndex;
use crate::{all_imports::TensorIndex, pyo3_prelude::*};

#[pyfunction]
pub fn batch_to_concat(circuit: CircuitRc, axis: usize, num_batches: usize) -> CircResult {
    let l = circuit.info().shape[axis];
    if l % num_batches != 0 {
        return Err(CircuitConstructionError::BatchNumberDoesntDivide { l, num_batches });
    }
    let batch_size = l / num_batches;
    let circuit = deep_map_unwrap(&circuit, |x| {
        x.as_index()
            .map(|x| Index::slice_edges_to_none(x).rc())
            .unwrap_or(x.clone().rc())
    });

    let (name, circuit, leaves_axis, leaves_non_axis) = get_axis_leaves(circuit, axis, true)?;
    // println!("leaves axis");
    // for (k, v) in &leaves_axis {
    //     println!("{}", v);
    //     k.compiler_print();
    // }
    // println!("leaves non axis");
    // for k in &leaves_non_axis {
    //     k.compiler_print();
    // }
    let input_specs_axis: Vec<(CircuitRc, ModuleNodeArgSpec)> = leaves_axis
        .iter()
        .map(|(sub, i)| {
            (
                sub.clone(),
                ModuleNodeArgSpec {
                    symbol: set_named_axes(
                        &Symbol::new_with_random_uuid(sub.info().shape.clone(), None),
                        BTreeMap::from([(*i as u8, name.clone())]),
                    ),
                    batchable: true,
                    expandable: true,
                },
            )
        })
        .collect();
    let input_specs: Vec<(CircuitRc, ModuleNodeArgSpec)> = input_specs_axis
        .iter()
        .cloned()
        .chain(leaves_non_axis.iter().map(|sub| {
            (
                sub.clone(),
                ModuleNodeArgSpec {
                    symbol: Symbol::new_with_random_uuid(sub.info().shape.clone(), None),
                    batchable: true,
                    expandable: true,
                },
            )
        }))
        .collect();
    // println!("input_specs");
    // for is in &input_specs {
    //     is.0.compiler_print();
    // }
    if input_specs.is_empty() {
        return Err(CircuitConstructionError::BatchAxisOriginatesTooHigh {});
    }
    let module_spec =
        ModuleNodeSpec::new_extract(circuit.clone(), input_specs.clone(), None, false)
            .ok_or(CircuitConstructionError::BatchAxisOriginatesTooHigh {})?;
    // println!("module spec");
    // module_spec.spec_circuit.compiler_print();
    let module_spec = module_spec.resize(
        module_spec
            .input_specs
            .iter()
            .map(|inp_spec| {
                if let Some((c, _is)) = input_specs_axis
                    .iter()
                    .find(|(_c, spec)| spec.symbol.uuid == inp_spec.symbol.uuid)
                {
                    let mut result = c.info().shape.clone();
                    result[leaves_axis[c]] = batch_size;
                    return result;
                }
                inp_spec.symbol.info().shape.clone()
            })
            .collect(),
    )?;
    // println!("module spec after resize");
    // module_spec.spec_circuit.compiler_print();
    let concattands: Vec<CircuitRc> = (0..num_batches)
        .map(|i| {
            let new_nodes: Vec<CircuitRc> = module_spec
                .input_specs
                .iter()
                .map(|inp_spec| {
                    if let Some((c, _is)) = input_specs_axis
                        .iter()
                        .find(|z| z.1.symbol.uuid == inp_spec.symbol.uuid)
                    {
                        return Index::nrc(
                            c.clone(),
                            TensorIndex::new_single(
                                TensorAxisIndex::new_plain_slice(
                                    i * batch_size,
                                    (i + 1) * batch_size,
                                ),
                                leaves_axis[c],
                                c.info().rank(),
                            ),
                            None,
                        );
                    }
                    input_specs
                        .iter()
                        .find(|(_c, s)| s.symbol.uuid == inp_spec.symbol.uuid)
                        .unwrap()
                        .0
                        .clone()
                })
                .collect();

            // println!("module args");
            // for c in new_nodes.iter() {
            //     c.compiler_print();
            // }
            ModuleNode::nrc(new_nodes, module_spec.clone(), None)
        })
        .collect();
    let result = Concat::nrc(concattands, axis, None);
    if result.info().shape != circuit.info().shape {
        println!(
            "shapes not equal {:?} {:?}",
            result.info().shape,
            circuit.info().shape
        );
        println!("old");
        circuit.compiler_print();
        println!("new");
        result.compiler_print();
        return Err(CircuitConstructionError::BugError {});
    }
    Ok(result)
}
