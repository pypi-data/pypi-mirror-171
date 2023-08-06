use rust_circuit::{
    circuit::{
        circuit_optimizer::{optimize_circuit, OptimizationContext, OptimizationSettings},
        deep_rewrite::compiler_simp,
        parse_compiler_repr_bijection,
    },
    rrfs::get_rrfs_dir,
};
use std::fs;

#[test]
fn benchmarking_circs() {
    fn item() {
        pyo3::prepare_freethreaded_python();

        dbg!("pre");
        let circuits: Vec<_> =
            fs::read_dir(format!("{}/ryan/compiler_benches/", get_rrfs_dir()))
                .unwrap()
                .map(|d| {
                    parse_compiler_repr_bijection(
                        &fs::read_to_string(d.unwrap().path()).unwrap(),
                        Default::default(),
                        Default::default(),
                        false,
                        Default::default(),
                    )
                    .unwrap()
                })
                .collect();
        dbg!("post");

        let mut settings: OptimizationSettings = Default::default();
        settings.verbose = 2;
        settings.log_simplifications = true;
        let mut context = OptimizationContext::new_settings(settings);
        for circuit in circuits {
            let result = optimize_circuit(circuit, &mut context);
            println!("{}", context.stringify_logs());
            // println!("{:?}", result.info().hash);
        }
    }
    std::thread::Builder::new()
        .stack_size(1024usize.pow(2) * 128)
        .spawn(item)
        .unwrap()
        .join()
        .unwrap();
}
