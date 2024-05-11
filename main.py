import os
import subprocess
import sys
from args_parser import get_shared_parser
import pkg_resources

def main():
    # 解析命令行参数
    parser = get_shared_parser()
    args = parser.parse_args()

    venv_name = "myenv\modelscope-down"
    python_path = sys.executable

    # 获取虚拟环境激活脚本路径
    activate_script = os.path.join(venv_name, "Scripts", "activate")

    # 检查虚拟环境是否存在
    if not os.path.exists(activate_script):
        print("虚拟环境不存在，正在创建虚拟环境 ...")
        # 创建虚拟环境
        subprocess.run([python_path, "-m", "venv", venv_name])    
    else:
        print("虚拟环境已存在")


    # 虚拟环境的 Python 解释器路径
    venv_python=os.path.join(venv_name, "Scripts", "python.exe")
    # 打印出 Python 解释器的路径，以确认是否是虚拟环境中的解释器
    print(f'虚拟环境的 Python 解释器路径: {venv_python}')

    # 在虚拟环境中安装 packages
    installed_packages = subprocess.check_output([venv_python, "-m", "pip", "list"], text=True)
    if 'modelscope' in installed_packages:
        print('已安装modelscope包')
    else:
        print('正在安装modelscope包 ...') 
        subprocess.run([venv_python, "-m", "pip", "install", "modelscope"])
        
    args_string = f"{args.model_name}"
    if args.version:
        args_string += f" --version {args.version}"
    if args.output_dir:
        args_string += f" --output_dir {args.output_dir}"    
    # 使用虚拟环境的 Python 解释器运行脚本   

    subprocess.run([venv_python, 'run_model_scope.py'] + args_string.split())

    # subprocess.run([venv_python, f'SampleModelDown.py {args_string}'])
    
if __name__ == "__main__":
    main()


