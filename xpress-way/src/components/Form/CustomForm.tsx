import 'bootstrap/dist/css/bootstrap.min.css';
import './CustomForm.css';
import { Form } from 'react-bootstrap';


export default function CustomForm() {
  return (
    <div className='form-div'>
      <Form className="credit-card-div mb-2">  
        <Form.Group className="mb-3 w-75" controlId="formCreditCardNumber">
          <Form.Label className='fs-2'>Credit Card Data</Form.Label>
          <Form.Control type="text" placeholder="Enter credit card number" />
        </Form.Group>
        
        <Form.Group className="mb-3 w-75 d-flex flex-row" controlId="formExpireDate">
          <Form.Control className='p-0 me-1' type="text" placeholder="MM/YY" />
          <Form.Control className='p-0 ms-1' type="text" placeholder="CVV" />
        </Form.Group>
      </Form>
      <h1 className='fs-2 total-div'>Total: $100</h1>
    </div>
  );
        
}