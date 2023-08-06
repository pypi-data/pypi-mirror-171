# mlpreprocessor

本库为为机器学习方法准备数据的工具类，同时提供命令行

# 打包上传
```bash
rm -r dist

rm -r src/ddd_objects.egg-info

python3 -m pip install --upgrade setuptools wheel twine build

python3 -m build

python3 -m twine upload dist/*
```
# 下载使用
```bash
pip install mlpreprocessor
```
```python
import mlpreprocessor
```