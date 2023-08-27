import './App.css';
import { useState, ChangeEvent } from 'react';
import cat from './images/cat.png';
import loadingGif from './images/loading.gif';

const apiWorksEnv = process.env.REACT_APP_API_WORKS ?? 'true';
const remoteApiWorks = (apiWorksEnv === 'true');
const ApiURL = process.env.REACT_APP_API_URL ?? 'http://0.0.0.0:8000/predict'

function App() {
    const [selectedImage, setSelectedImage] = useState<string | null>(null);
    const [classificationResult, setClassificationResult] = useState<string | null>(null);
    const [loading, setLoading] = useState<boolean>(false);

    const handleImageChange = (event: ChangeEvent<HTMLInputElement>) => {
        setClassificationResult(null);
        const file = event.target.files?.[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = () => {
                setSelectedImage(reader.result as string);
            };
            reader.readAsDataURL(file);
        }
    };

    const handleImageUpload = async () => {
        if (!remoteApiWorks) {
            alert("The actual classification won't work on production, because I stopped paying for the Heroku server. ;)");
            return; // Return early to avoid the rest of the function
        }

        if (!selectedImage) {
            alert("Please select an image first.");
            return;
        }

        try {
            setLoading(true);

            const formData = new FormData();
            formData.append('image', dataURItoBlob(selectedImage));

            const response = await fetch(ApiURL, {

                method: 'POST',
                body: formData,
            });

            const data = await response.json();
            console.log('Response Data:', data);
            setClassificationResult(data.predicted_class);
        } catch (error) {
            console.error('Error uploading image:', error);
        } finally {
            setLoading(false);
        }
    };

    function dataURItoBlob(dataURI: string): Blob {
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
            <button className={`upload-row ${!selectedImage ? 'invisible' : ''}`} onClick={handleImageUpload}>Classify Image</button>
            {selectedImage
                ?
                <img src={selectedImage} alt="Selected" />
                :
                <img src={cat} alt="cat" />}
            <div className="upload-row">
                <p>Classification Result:&nbsp;</p>
                <p>
                    {!selectedImage
                        ? "Cat"
                        : loading
                            ? <img className="gif" src={loadingGif} alt="loading" />
                            : classificationResult
                                ? "Cat"
                                : ""
                    }
                </p>
            </div>
        </div>
    );
}

export default App;
