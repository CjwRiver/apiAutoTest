from test.conftest import pytest
from tools import logger
from tools.read_file import ReadFile
from tools.send_email import EmailServe
import os
import shutil

report = ReadFile.read_config('$.file_path.report')
logfile = ReadFile.read_config('$.file_path.log')
file_path = ReadFile.read_config('$.file_path')
email = ReadFile.read_config('$.email')


def run():
    if os.path.exists('report/'):
        shutil.rmtree(path='report/')
    logger.add(logfile, enqueue=True, encoding='utf-8')
    # logger.add(file_path['log'], enqueue=True, encoding='utf-8')
    logger.info("""
                          _     _                  
                          | |   (_)                 
     _   _ _   _ _ __  ___| |__  ___  ___   _ _ __  
    | | | | | | | '_ \/ __| '_ \| \ \/ / | | | '_ \ 
    | |_| | |_| | | | \__ \ | | | |>  <| |_| | | | |
     \__, |\__,_|_| |_|___/_| |_|_/_/\_\\__,_|_| |_|
      __/ |                                         
     |___/ 
    """)
    pytest.main(args=['test/test_api.py', f'--alluredir={report}/data'])
    pytest.main(args=['test/test_api.py', f'--alluredir={file_path["report"]}/data'])
    # 自动以服务形式打开报告
    # os.system(f'allure serve {report}/data')

    # 本地生成报告
    os.system(f'allure generate {report}/data -o {report}/html --clean')
    os.system(f'allure generate {file_path["report"]}/data -o {file_path["report"]}/html --clean')
    logger.success('报告已生成')

    # 发送邮件带附件报告
    # EmailServe.send_email(email, file_path['report'])

# if __name__ == '__main__':
#    run()
#    # 删除本地附件
#    os.remove(email['enclosures'])


if __name__ == '__main__':
    run()