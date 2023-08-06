### ojitos369 (General)
[REPO: https://github.com/Ojitos369/ojitos369-pip](https://github.com/Ojitos369/ojitos369-pip)

### FTP

```py

from ojitos369_ftp.ftp import ConnectionFtp

ftp_data = {
    'host': 'your_ftp_host',
    'port': 'your_ftp_port',
    'user': 'your_ftp_user',
    'password': 'your_ftp_password',
}
ftp = ConnectionFtp(ftp_data)

ftp.mkdir('some_path')
ftp.cd('some_path')

ftp.upload('~/files/your.file', '.'): # upload your.file into some_path (ftp)
ftp.ls()
# >> ['your.file']
ftp.cd('..')
ftp.clear_dir('some_path')
ftp.ls('some_path')
# >> []

ftp.rmdir('some_path')


ftp.rm('some.file')

ftp.pwd()
# >> 'actual_ftp_dir

ftp.rename('your.file', 'your_2.file')
ftp.mv('your.file', 'some_path')

ftp.ls('some_path')
# >> ['your.file', 'your_2.file']
ftp.ls('some_path_2')
# >> []

ftp.mv_files('some_path', 'some_path_2')
ftp.ls('some_path')
# >> []
ftp.ls('some_path_2')
# >> ['your.file', 'your_2.file']

ftp.cp('some_path/your.file', '~/files/your.file')

ftp.close()


```