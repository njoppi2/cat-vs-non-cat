import './App.css';
import React, { useState, useEffect } from 'react';
import cat from './images/cat.png'
import loadingGif from './images/loading.gif'


function App() {
    const [selectedImage, setSelectedImage] = useState(null);
    const [classificationResult, setClassificationResult] = useState(null);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        console.log("selectedImage: " + !!selectedImage)
        console.log("classificationResult: " + !!classificationResult)
    }, [classificationResult, selectedImage]);

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
                setLoading(true);
                const formData = new FormData();
                formData.append('image', dataURItoBlob(selectedImage)); // Convert data URI to Blob

                const response = await fetch('https://cat-app-github-beab32ceaa08.herokuapp.com/predict', {
                    method: 'POST',
                    body: formData,
                });

                const data = await response.json();
                console.log('Response Data:', data);
                setClassificationResult(data.predicted_class);
                setLoading(false);
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
            <div className="App-header">Cat classifier<p className="small">(Simple)</p></div>
            <div className="upload-row">
                <p className="upload-image">Upload an image:&nbsp;</p>
                <input type="file" accept="image/*" onChange={handleImageChange} />
            </div>
            <button className="upload-row" onClick={handleImageUpload}>Classify Image</button>
            {selectedImage
                ?
                <img src={selectedImage} alt="Selected" />
                :
                <img src={cat} alt="cat" />}
            <div className="upload-row">
                <p>Classification Result:&nbsp;</p>
                <p>
                    {!selectedImage ? "Cat" : (classificationResult === null) ? (loading && <img className="gif" src={loadingGif} alt="loading" />) : (classificationResult ? "Cat" : "Not a cat")}
                </p>
            </div>
        </div>
    );
}

export default App;
