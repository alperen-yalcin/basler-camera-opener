from pypylon import pylon
import cv2

target_serial = "24068739"
available_cameras = pylon.TlFactory.GetInstance().EnumerateDevices()
camera_found = False

for cam_info in available_cameras:
    if cam_info.GetSerialNumber() == target_serial:
        camera = pylon.InstantCamera(pylon.TlFactory.GetInstance().CreateDevice(cam_info))
        camera.Open()
        camera.StartGrabbing(pylon.GrabStrategy_LatestImageOnly)

        converter = pylon.ImageFormatConverter()
        converter.OutputPixelFormat = pylon.PixelType_Mono8
        converter.OutputBitAlignment = pylon.OutputBitAlignment_MsbAligned

        camera_found = True
        print("Starting live video. Press 'q' to exit.")

        while camera.IsGrabbing():
            grab_result = camera.RetrieveResult(5000, pylon.TimeoutHandling_ThrowException)
            if grab_result.GrabSucceeded():
                image = converter.Convert(grab_result)
                img_array = image.GetArray()

                cv2.imshow("Basler Camera", img_array)
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
            grab_result.Release()

        camera.StopGrabbing()
        camera.Close()
        cv2.destroyAllWindows()
        break

if not camera_found:
    print("No camera with specified serial number found.")
