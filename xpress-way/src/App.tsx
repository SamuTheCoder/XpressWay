import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import './components/Form/CustomForm.tsx'
import CustomForm from './components/Form/CustomForm.tsx'
import Header from './components/Header/Header.tsx'
import { Button } from 'react-bootstrap'

function App() {
  const [count, setCount] = useState(0)

  return (
    <>
      <Header/>
      <div className="form-container m-3 p-2">
          <CustomForm/>
          <Button variant="success" type="submit" className="w-25 fs-3">
          Pay
          </Button>
      </div>
      <p className="bottom-label">
        Maximum security for your payments
      </p>
    </>
  )
}

export default App
