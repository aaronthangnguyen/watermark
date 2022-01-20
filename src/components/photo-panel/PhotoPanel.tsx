import { Box, Image } from '@chakra-ui/react';

const PhotoPanel = () => {
  return (
    <Box height="max-content" width="60%">
      <Image
        src="https://source.unsplash.com/random/1920x1080"
        rounded="base"
        shadow="lg"
        pointerEvents="none"
        userSelect="none"
      />
    </Box>
  );
};

export default PhotoPanel;
