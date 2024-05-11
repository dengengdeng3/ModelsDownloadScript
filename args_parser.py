import argparse
def get_shared_parser():
    parser = argparse.ArgumentParser(description='大语言模型下载（自动创建虚环境，不影响系统依赖）')
    parser.add_argument('model_name', type=str, help='模型名称')
    parser.add_argument('--version', '-v', type=str, default=None, help='模型版本，默认不指定')
    parser.add_argument('--output_dir', '-o', type=str, default='./', help='模型存放路径，默认为当前路径')
    return parser
