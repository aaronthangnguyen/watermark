import { extendTheme } from '@chakra-ui/react';

const theme = extendTheme({
  fonts: {
    heading: 'Cabin',
    body: 'Cabin',
  },
  styles: {
    global: {
      body: {
        bgGradient: 'linear(to-r, teal.500, green.500)',
      },
    },
  },
});

export default theme;
