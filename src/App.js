import './App.css';
import React, { useState } from 'react';

function App() {
    const [selectedImage, setSelectedImage] = useState(null);

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

    return (
        <div className="App">
            <div className="App-header">Cat classifier</div>
            <div className="upload-row">
                <p>Upload an image:&nbsp;</p>
                <input type="file" accept="image/*" onChange={handleImageChange} />
            </div>
            {selectedImage && <img src={selectedImage} alt="Selected" />}
        </div>
    );
}

export default App;
