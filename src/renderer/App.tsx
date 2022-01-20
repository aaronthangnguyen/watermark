import { ChakraProvider, Flex } from '@chakra-ui/react';
import '@fontsource/cabin';
import '@fontsource/pacifico';
import Title from 'components/common/Title';
import ControlPanel from 'components/control-panel/ControlPanel';
import PhotoPanel from 'components/photo-panel/PhotoPanel';
import { MemoryRouter as Router, Route, Routes } from 'react-router-dom';
import theme from './theme';

const Main = () => {
  return (
    <Flex direction="column" m="2rem">
      <Title />
      <Flex gap="2rem">
        <PhotoPanel />
        <ControlPanel />
      </Flex>
    </Flex>
  );
};

export default function App() {
  return (
    <ChakraProvider theme={theme}>
      <Router>
        <Routes>
          <Route path="/" element={<Main />} />
        </Routes>
      </Router>
    </ChakraProvider>
  );
}
