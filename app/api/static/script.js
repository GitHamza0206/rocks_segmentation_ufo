document.querySelector('button').addEventListener('click', function() {
        var input = document.querySelector('input[type="file"]');
        var data = new FormData();
        data.append('image', input.files[0]);
    
        fetch('/remove_background', {
            method: 'POST',
            body: data
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('results').innerHTML = `
                <p>UFO detected: ${data.ufo_detected ? 'Yes' : 'No'}</p>
            `;
        });
    });

    tailwind.config = {
        theme: {
            extend: {
                animation: {
                    fadeIn: 'fadeIn 1.5s ease-in-out',
                    slideUp: 'slideUp 0.5s ease-in-out',
                }
            }
        }
    }

        const dropArea = document.getElementById('drop-area');
        const fileElem = document.getElementById('fileElem');
        const preview = document.getElementById('preview');
        const previewImage = document.getElementById('preview-image');
        const detectButton = document.getElementById('detectButton');
        const results = document.getElementById('results');
    
        ['dragenter', 'dragover', 'dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, preventDefaults, false);
        });
    
        function preventDefaults(e) {
            e.preventDefault();
            e.stopPropagation();
        }
    
        ['dragenter', 'dragover'].forEach(eventName => {
            dropArea.addEventListener(eventName, highlight, false);
        });
    
        ['dragleave', 'drop'].forEach(eventName => {
            dropArea.addEventListener(eventName, unhighlight, false);
        });
    
        function highlight() {
            dropArea.classList.add('border-indigo-500', 'bg-gray-50');
        }
    
        function unhighlight() {
            dropArea.classList.remove('border-indigo-500', 'bg-gray-50');
        }
    
        dropArea.addEventListener('drop', handleDrop, false);
    
        function handleDrop(e) {
            const dt = e.dataTransfer;
            const files = dt.files;
            handleFiles(files);
        }
    
        function handleFiles(files) {
            if (files.length > 0) {
                const file = files[0];
                previewFile(file);
                detectButton.disabled = false;
            }
        }
    
        function previewFile(file) {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onloadend = function() {
                preview.classList.remove('hidden');
                previewImage.src = reader.result;
            }
        }
    
        detectButton.addEventListener('click', function() {
            const file = fileElem.files[0];
            if (!file) return;
    
            const formData = new FormData();
            formData.append('image', file);
    
            results.innerHTML = '<p class="text-gray-600">Processing... Please wait.</p>';
    
            fetch('/remove_background', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);
                if (data.report_url) {
                    results.innerHTML = `
                        <p class="text-green-600 mb-4">Detection complete! Your report is ready.</p>
                        <a href="${data.report_url}" target="_blank" class="bg-indigo-600 text-white px-4 py-2 rounded-md hover:bg-indigo-700 transition duration-300">
                            View PDF Report
                        </a>
                    `;
                } else {
                    results.innerHTML = '<p class="text-red-600">An error occurred while generating the report. Please try again.</p>';
                }
            })
            .catch(error => {
                console.error('Error:', error);
                results.innerHTML = '<p class="text-red-600">An error occurred. Please try again.</p>';
            });
        });

document.querySelector('button').addEventListener('click', function() {
const fileInput = document.querySelector('input[type="file"]');
const scalingFactor = document.getElementById('scaling-factor').value;

if (!fileInput.files.length || !scalingFactor) {
    alert("Veuillez télécharger une image et définir le facteur d'échelle");
    return;
}

const file = fileInput.files[0];
const formData = new FormData();
formData.append('image', file);
formData.append('scaling_factor', scalingFactor);

// Votre code fetch existant pour envoyer les données au backend
// ...
});