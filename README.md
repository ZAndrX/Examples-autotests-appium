# Examples-autotests-appium
### Документация по настройке appium сервера: <br/>
https://developer.android.com/tools/adb#wireless <br/>
https://hub.docker.com/r/appium/appium/

### Для запуска appium сервера можете использовать:

 `docker run -d -p 4723:4723 -e REMOTE_ADB=true -e ANDROID_DEVICES=192.168.31.1:5555 -e REMOTE_ADB_POLLING_SEC=60`
 
### Для запуска тестов используйте:

`pytest -sv --udid=192.168.31.1:5555 --url=http://127.0.0.1:4723` <br/>

Описание аргументов: <br/>
`--udid` идентификатор устройства (имя устройства в adb devices) <br/>
`--url` домен appium сервера