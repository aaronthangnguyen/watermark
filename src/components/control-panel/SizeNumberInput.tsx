import {
  FormControl,
  FormLabel,
  NumberDecrementStepper,
  NumberIncrementStepper,
  NumberInput,
  NumberInputField,
  NumberInputStepper,
} from '@chakra-ui/react';

function SizeNumberInput() {
  return (
    <FormControl>
      <FormLabel fontWeight="bold" htmlFor="size">
        Size
      </FormLabel>

      <NumberInput
        id="size"
        width="5.5rem"
        min={0}
        max={100}
        defaultValue={20}
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

export default SizeNumberInput;
