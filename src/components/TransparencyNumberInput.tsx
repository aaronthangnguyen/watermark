import {
  FormControl,
  FormLabel,
  NumberDecrementStepper,
  NumberIncrementStepper,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
} from '@chakra-ui/react';

function TransparencyNumberInput() {
  return (
    <FormControl>
      <FormLabel fontWeight="bold" htmlFor="size">
        Transparency
      </FormLabel>

      <NumberInput
        id="size"
        width="5.5rem"
        min={0}
        max={100}
        defaultValue={100}
        precision={0}
        step={5}
      >
        <NumberInputField />
        <NumberInputStepper>
          <NumberIncrementStepper />
          <NumberDecrementStepper />
        </NumberInputStepper>
      </NumberInput>
    </FormControl>
  );
}

export default TransparencyNumberInput;
