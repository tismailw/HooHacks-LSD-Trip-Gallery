document.addEventListener('DOMContentLoaded', function() {
    const gallery = document.getElementById('gallery');
    const modal = document.getElementById('modal');
    const modalContent = document.getElementById('modal-content'); // Change modalImg to modalContent
    const captionText = document.getElementById('caption');
    const closeBtn = document.getElementsByClassName('close')[0];
  
    const videos = [
        'trip1.mp4',
        'trip2.mp4',
        'trip3.mp4',
        'trip4.mp4',
        'trip5.mp4',
        // ... any additional video files
    ];
      
    videos.forEach((src, index) => {
      const videoElement = document.createElement('video');
      const sourceElement = document.createElement('source');
  
      sourceElement.src = src;
      sourceElement.type = 'video/mp4';
  
      videoElement.appendChild(sourceElement);
      videoElement.controls = true; // Add controls to the video
      videoElement.style.width = '100%'; // Set a default width or customize as needed
      videoElement.alt = `Artwork ${index + 1}`; // alt attribute is not valid for video, consider using a data attribute or title
  
      videoElement.addEventListener('click', function() {
        modal.style.display = 'block';
        modalContent.innerHTML = ''; // Clear previous content
        const modalVideo = videoElement.cloneNode(true); // Clone the video element to play in the modal
        modalContent.appendChild(modalVideo); // Append the cloned video to the modal content
        modalVideo.play(); // Play the video
        captionText.innerHTML = this.alt; // Use a different attribute or method to get the caption
      });
  
      gallery.appendChild(videoElement);
    });
  
    closeBtn.addEventListener('click', function() {
      modal.style.display = 'none';
      modalContent.innerHTML = ''; // Stop the video and clear the content when closing the modal
    });
  });