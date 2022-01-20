import {
  RadioGroup,
  Radio,
  Stack,
  FormControl,
  FormLabel,
} from '@chakra-ui/react';

const PositionRadioInput = () => {
  return (
    <FormControl>
      <FormLabel fontWeight="bold">Position</FormLabel>
      <RadioGroup defaultValue="1">
        <Stack direction="column">
          <Radio value="1">Top Left</Radio>
          <Radio value="2">Top Right</Radio>
          <Radio value="3">Bottom Right</Radio>
          <Radio value="4">Bottom Left</Radio>
        </Stack>
      </RadioGroup>
    </FormControl>
  );
};

export default PositionRadioInput;
