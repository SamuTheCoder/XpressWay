import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import './components/Form/CustomForm.tsx'
import CustomForm from './components/Form/CustomForm.tsx'
import Header from './components/Header/Header.tsx'
import { Button, Alert } from 'react-bootstrap'

function App() {
  const [status, setStatus] = useState("Awaiting Payment");
  const [loading, setLoading] = useState(false);
  const [message, setMessage] = useState<{ type: "success" | "danger" | ""; text: string }>({ type: "", text: "" });

  const paymentId = "67e3525bc8bce8b95833cc76"; // Replace with actual ID

  const handlePayment = async () => {
    setLoading(true);
    setStatus("Processing...");

    setTimeout(async () => {
      try {
        const response = await fetch(`http://localhost:5000/v1/payments/${paymentId}/confirm`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
        });

        if (!response.ok) {
          throw new Error("Failed to confirm payment");
        }

        setStatus("Payment Successful");
        setMessage({ type: "success", text: "Your payment was confirmed successfully!" });
      } catch (error) {
        console.error("Error confirming payment:", error);
        setStatus("Payment Failed");
        setMessage({ type: "danger", text: "There was an issue confirming your payment. Please try again." });
      } finally {
        setLoading(false);
      }
    }, 2000);
  };


  return (
    <>
      <Header/>
      <div className="form-container m-3 p-2">
          <CustomForm/>
          <Button variant="success" type="submit" className="w-25 fs-3" onClick={handlePayment}>
          Pay
          </Button>
        {message.text && <Alert variant={message.type} className="mt-3">{message.text}</Alert>}
      </div>
      <p className="bottom-label">
        Maximum security for your payments
      </p>
    </>
  )
}

export default App
