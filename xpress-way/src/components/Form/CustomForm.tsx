import 'bootstrap/dist/css/bootstrap.min.css';
import './CustomForm.css';
import { Form } from 'react-bootstrap';
import { useState } from 'react';


export default function CustomForm({ onInputChange }: { onInputChange: (field: string, value: string) => void }) {
  const [creditCard, setCreditCard] = useState('');
  const [expireDate, setExpireDate] = useState('');
  const [cvv, setCvv] = useState('');

  const handleInputChange = (field: string, value: string) => {
    onInputChange(field, value); // Send input data to parent
  };

  return (
    <div className='form-div'>
      <Form className="credit-card-div mb-2">  
        <Form.Group className="mb-3 w-75" controlId="formCreditCardNumber">
          <Form.Label className='fs-2'>Credit Card Data</Form.Label>
          <Form.Control 
            type="text" 
            placeholder="Enter credit card number"
            value={creditCard}
            onChange={(e) => {
              setCreditCard(e.target.value);
              handleInputChange("creditCard", e.target.value);
            }}
          />
        </Form.Group>
        
        <Form.Group className="mb-3 w-75 d-flex flex-row" controlId="formExpireDate">
          <Form.Control 
            className='p-0 me-1' 
            type="text" 
            placeholder="MM/YY" 
            value={expireDate}
            onChange={(e) => {
              setExpireDate(e.target.value);
              handleInputChange("expireDate", e.target.value);
            }}
          />
          <Form.Control 
            className='p-0 ms-1' 
            type="text" 
            placeholder="CVV" 
            value={cvv}
            onChange={(e) => {
              setCvv(e.target.value);
              handleInputChange("cvv", e.target.value);
            }}
          />
        </Form.Group>
      </Form>
      <h1 className='fs-2 total-div'>Total: $100</h1>
    </div>
  );
        
}