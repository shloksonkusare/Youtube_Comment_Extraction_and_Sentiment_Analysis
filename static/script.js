function extractVideoId(input) {
  if (!input) return null;
  input = input.trim();
  const patterns = [
    /(?:https?:\/\/)?(?:www\.)?youtube\.com\/watch\?v=([\w-]{11})/,
    /(?:https?:\/\/)?youtu\.be\/([\w-]{11})/,
    /^([\w-]{11})$/
  ];
  for (const p of patterns) {
    const match = input.match(p);
    if (match && match[1]) return match[1];
  }
  return null;
}

function previewVideo() {
  const url = document.getElementById('videoUrl').value;
  const videoId = extractVideoId(url);
  if (!videoId) {
    alert('Invalid YouTube link');
    return;
  }
  const thumb = document.getElementById('thumb');
  thumb.style.backgroundImage = `url(https://img.youtube.com/vi/${videoId}/hqdefault.jpg)`;
}

function extractComments() {
  const url = document.getElementById('videoUrl').value;
  const videoId = extractVideoId(url);

  if (!videoId) {
    alert('Invalid YouTube link');
    return;
  }

  // Create a hidden form to trigger file download
  const form = document.createElement('form');
  form.method = 'POST';
  form.action = '/extract_comments';

  const input = document.createElement('input');
  input.type = 'hidden';
  input.name = 'youtube_link';
  input.value = url;

  form.appendChild(input);
  document.body.appendChild(form);
  form.submit();
}
