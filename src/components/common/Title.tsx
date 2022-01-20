import { Heading } from '@chakra-ui/react';

const Title = () => {
  return (
    <div>
      <Heading
        size="2xl"
        mb="3rem"
        sx={{ fontFamily: 'Pacifico', letterSpacing: 1 }}
      >
        Watermark 🐁
      </Heading>
    </div>
  );
};

export default Title;
