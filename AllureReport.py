from Common import Log
from Common import Shell
import os

if __name__ == '__main__':
    log = Log.MyLog()

    shell = Shell.Shell()
    report_path = str(os.path.dirname(os.path.abspath(__file__)))
    xml_report_path = report_path + '\\Report\\xml'
    html_report_path = report_path + '\\Report\\html --clean'

    # 使用Jenkins执行时，会自动生成allure的HTML报告，故废弃以下生成报告代码
    allLine_path = 'D:\\allure-2.16.1\\bin\\allure.bat'


    cmd = allLine_path + ' generate %s -o %s' % (xml_report_path, html_report_path)
    print(cmd)
    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

