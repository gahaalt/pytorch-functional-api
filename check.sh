# Copyright (c) 2022 Szymon Mikler

echo "Running test suite for pytorch-symbolic!"
echo "Optional dependencies are required. Install using 'pip install pytorch-symbolic[full]'"
echo ""

echo "Running isort..."
isort .

echo "Running black..."
black .

echo "Running flake8..."
flake8 .

echo "Running mypy..."
mypy .

echo "Running pytest with the default settings..."
pytest --no-header . || exit

echo "Running pytest with codegen active..."
export PYTORCH_SYMBOLIC_CODEGEN_MIN_LOOP_LENGTH=2
pytest --no-header . || exit

echo "Running pytest with codegen disabled..."
export PYTORCH_SYMBOLIC_CODEGEN_BY_DEFAULT=False
pytest --no-header . || exit
