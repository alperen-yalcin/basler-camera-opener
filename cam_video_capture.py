from pypylon import pylon

target_serial = "12345678"
available_cameras = pylon.TlFactory.GetInstance().EnumerateDevices()
camera_found = False

for cam_info in available_cameras:
    if cam_info.GetSerialNumber() == target_serial:
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(cam_info))
        camera.Open()
        camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)
        print("The camera turned on and started capturing images.")
        camera_found = True
        break

if not camera_found:
    print("No camera with specified serial number.")
