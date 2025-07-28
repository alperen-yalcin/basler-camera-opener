from pypylon import pylon
import cv2

target_serial = '24068739'

def get_camera_by_serial(serial_number):
    available_cameras = pylon.TlFactory.GetInstance().EnumerateDevices()
    for cam_info in available_cameras:
        if cam_info.GetSerialNumber() == serial_number:
            camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(cam_info))
            camera.Open()
            print(f'Camera turned on: {camera.GetDeviceInfo().GetModelName()}')
            return camera
    print('No camera with specified serial number found.')
    return None