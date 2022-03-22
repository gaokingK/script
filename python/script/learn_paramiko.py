"""
# 问题
- OSError: Failure 是因为远端地址路径不对（路径中的文件夹要存在，并且不能缺少文件名， 可以改名）
Traceback (most recent call last):
  File "C:\Users\Administrator\Desktop\people_lab_win\record_542N2\record_server.py", line 114, in put_sftp
    sftp.put(file_path, remote_file_path)
  File "C:\python_env\record542N2\lib\site-packages\paramiko\sftp_client.py", line 759, in put
    return self.putfo(fl, remotepath, file_size, callback, confirm)
  File "C:\python_env\record542N2\lib\site-packages\paramiko\sftp_client.py", line 714, in putfo
    with self.file(remotepath, "wb") as fr:
  File "C:\python_env\record542N2\lib\site-packages\paramiko\sftp_client.py", line 372, in open
    t, msg = self._request(CMD_OPEN, filename, imode, attrblock)
  File "C:\python_env\record542N2\lib\site-packages\paramiko\sftp_client.py", line 822, in _request
    return self._read_response(num)
  File "C:\python_env\record542N2\lib\site-packages\paramiko\sftp_client.py", line 874, in _read_response
    self._convert_status(msg)
  File "C:\python_env\record542N2\lib\site-packages\paramiko\sftp_client.py", line 907, in _convert_status
    raise IOError(text)

# 使用
- sftp发送文件
"""

"""
To: 使用sftp发送文件
"""
import paramiko
def put_sftp(remote_ip, username, passwd, file_path, remote_file_path):
    """
    remote_file_path: 远端路径，是带文件名的
    """
    scp = paramiko.Transport(remote_ip, 22)
    print("scp  ok")
    try:
        scp.connect(username=username, password=passwd)
        sftp = paramiko.SFTPClient.from_transport(scp)
        sftp.put(file_path, remote_file_path)
        return True
    except Exception as e:
        print(e)
        logging.info(msg=e, exc_info=True, stack_info=True)
        return False
    finally:
        scp.close()