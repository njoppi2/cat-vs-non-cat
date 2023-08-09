import './App.css';
import React, { useState } from 'react';

function App() {
    const [selectedImage, setSelectedImage] = useState(null);
    const [classificationResult, setClassificationResult] = useState(null);

    const handleImageChange = (event) => {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                setSelectedImage(reader.result);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleImageUpload = async () => {
        if (selectedImage) {
            try {
                const formData = new FormData();
                formData.append('image', dataURItoBlob(selectedImage)); // Convert data URI to Blob

                const response = await fetch('http://njoppi2.duckdns.org:8000/predict', {
                    method: 'POST',
                    body: formData,
                });

                const data = await response.json();
                console.log('Response Data:', data);
                setClassificationResult(data.predicted_class);
            } catch (error) {
                console.error('Error uploading image:', error);
            }
        }
    };

    // Helper function to convert data URI to Blob
    function dataURItoBlob(dataURI) {
        const byteString = atob(dataURI.split(',')[1]);
        const mimeString = dataURI.split(',')[0].split(':')[1].split(';')[0];
        const ab = new ArrayBuffer(byteString.length);
        const ia = new Uint8Array(ab);
        for (let i = 0; i < byteString.length; i++) {
            ia[i] = byteString.charCodeAt(i);
        }
        return new Blob([ab], { type: mimeString });
    }


    return (
        <div className="App">
            <div className="App-header">Cat classifier</div>
            <div className="upload-row">
                <p>Upload an image:&nbsp;</p>
                <input type="file" accept="image/*" onChange={handleImageChange} />
                <button onClick={handleImageUpload}>Classify Image</button>
            </div>
            {selectedImage && <img src={selectedImage} alt="Selected" />}
            {classificationResult && (
                <div className="result">
                    <p>Classification Result:</p>
                    <p>{classificationResult}</p>
                </div>
            )}
        </div>
    );
}

export default App;
