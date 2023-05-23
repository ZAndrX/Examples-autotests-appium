# Examples-autotests-appium
https://developer.android.com/tools/adb#wireless 

https://hub.docker.com/r/appium/appium/

Connect all devices to docker physical machine

Run adb devices

Authorize all devices (do not forget to check Always allow this computer)

 `docker run -d -p 4723:4723 -e REMOTE_ADB=true -e ANDROID_DEVICES=192.168.31.60:5555 -e REMOTE_ADB_POLLING_SEC=60`