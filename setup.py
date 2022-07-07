from setuptools import setup
from setuptools_rust import Binding, RustExtension

setup(
    name="pybulletproofs",
    version="0.1.0-dev7",
    rust_extensions=[RustExtension(
        "pybulletproofs", binding=Binding.PyO3)],
    python_requires=">=3.7,<3.10",
    setup_requires="setuptools-rust == 0.12.1",
)
