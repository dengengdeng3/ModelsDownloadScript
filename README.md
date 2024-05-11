# 模型下载脚本目前支持ModelScope模型下载

## python main.py -h
大语言模型下载（自动创建虚环境，不影响系统依赖）

positional arguments:
  model_name            模型名称

options:
  -h, --help            show this help message and exit
  --version VERSION, -v VERSION
                        模型版本，默认不指定
  --output_dir OUTPUT_DIR, -o OUTPUT_DIR
                        模型存放路径，默认为当前路径

## python main.py qwen/Qwen1.5-14B

- 下载Qwen1.5-14B模型