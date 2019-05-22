# 电脑端的二维码解决方案
这个项目实现了在Linux下生成二维码和通过摄像头识别二维码。
## 说明
`generator.py`: 使用剪贴板的数据生成二维码。
`scanner.py`: 从摄像头得到得到图片, 将解码后的数据存在系统的剪贴板。解码成功发出提示音。30s内镜头中没有出现二维码，程序自动退出。

## 将程序添加到菜单
在Linux下可以通过以下方式完成:
```bash
sudo gedit /usr/share/applications/barcode_scanner.desktop
```
```
[Desktop Entry]
Encoding=UTF-8
Exec=/home/your/python/path/python /home/your/path/scanner.py
Icon=/usr/your/icon.svg
Type=Application
Terminal=false
Comment=Use camera to scann barcode, and save results to clipboard.
Name=barcode-scanner
GenericName=Use camera to scann barcode, and save results to clipboard.
StartupNotify=true
Categories=Development;
```
