# 📱 iOS Line Detection App

This guide provides detailed instructions for setting up the iOS app that interacts with the Python backend to perform line detection on images.

## 🛠️ Prerequisites

- Xcode installed on your Mac.
- Basic knowledge of Swift and iOS development.
- The Python backend server should be running.

## 🚀 Steps to Create the iOS App

1. **Create a New Xcode Project:**
   - Open Xcode and select "Create a new Xcode project."
   - Choose "App" under iOS and click "Next."
   - Enter the product name (e.g., "LineDetectionApp") and other details. Ensure the language is set to Swift.
   - Choose a location to save the project and click "Create."

2. **Set Up Permissions:**
   - Open `Info.plist` in your project.
   - Add a new key `Privacy - Photo Library Usage Description` with a description like "This app requires access to your photo library to select images."

3. **Design the User Interface:**
   - Open `Main.storyboard`.
   - Add a `UIButton` for selecting an image.
   - Add a `UIImageView` to display the selected and processed images.
   - Add a `UIButton` to save the processed image back to the Photos app.

4. **Implement Image Selection:**
   - Use `UIImagePickerController` to allow users to select an image from the Photos app.
   - Implement the delegate methods to handle image selection and display the image in the `UIImageView`.

5. **Upload Image to Backend:**
   - Use `URLSession` to upload the selected image to the Python backend.
   - Handle the response to receive the processed image.

6. **Display and Save Processed Image:**
   - Display the processed image in the `UIImageView`.
   - Implement functionality to save the processed image back to the Photos app using `UIImageWriteToSavedPhotosAlbum`.

7. **Run the App:**
   - Connect your iPhone or use the simulator to run the app.
   - Test the functionality to ensure images are processed and saved correctly.

## 📚 Additional Resources

- [Apple Developer Documentation](https://developer.apple.com/documentation/)
- [Swift by Sundell](https://www.swiftbysundell.com/)