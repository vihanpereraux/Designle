import extractColors from 'extract-colors'

const src = 'my-image.jpg'

extractColors(src)
  .then(console.log)
  .catch(console.error)