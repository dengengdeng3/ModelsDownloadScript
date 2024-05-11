import os
import argparse
import pkg_resources
from modelscope.hub.snapshot_download import snapshot_download
from args_parser import get_shared_parser


# 解析命令行参数
parser = get_shared_parser()
args = parser.parse_args()

# 使用命令行参数下载模型
model_dir = snapshot_download(
    args.model_name,
    args.version,
    cache_dir=args.output_dir
)

print(f'模型已下载到: {model_dir}')

