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

def capture_image(camera):
    camera.StartGrabbingMax(1)

    converter = pylon.ImageFormatConverter()
    converter.OutputPixelFormat = pylon.PixelType_Mono8
    converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

    while camera.IsGrabbing():
        grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
        if grab_result.GrabSucceeded():
            image = converter.Convert(grab_result)
            img_array = image.GetArray()
            print('Image taken.')
        grab_result.Release()
        return img_array

def show_image_and_cleanup(img_array, camera):
    cv2.imshow('Basler Camera View', img_array)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    camera.Close()
    print("Camera closed and window destroyed.")


