import { Box, Button, Flex } from '@chakra-ui/react';
import PositionRadioInput from 'components/PositionRadioInput';
import SizeNumberInput from 'components/SizeNumberInput';
import TransparencyNumberInput from 'components/TransparencyNumberInput';

const ControlPanel = () => {
  return (
    <Box width="40%">
      <Flex
        bg="white"
        p="1rem"
        rounded="base"
        shadow="lg"
        mb="1rem"
        gap="0.5rem"
      >
        <Button>Folder</Button>
        <Button>Logo</Button>
        <Button colorScheme="teal">Watermark</Button>
      </Flex>
      <Flex
        direction="column"
        bg="white"
        p="1rem"
        rounded="base"
        shadow="lg"
        gap="1rem"
      >
        <SizeNumberInput />
        <TransparencyNumberInput />
        <PositionRadioInput />
      </Flex>
    </Box>
  );
};

export default ControlPanel;
