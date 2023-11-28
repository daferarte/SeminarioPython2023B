import {BrowserRouter, Routes, Route, Link, Outlet, useParams} from 'react-router-dom';
import { Provider } from 'react-redux';
import { store } from './store';
import SignIn from './recolector/SingIn';

let Hello=()=>{
  return <h1>Saludo Estudiantes</h1>
};

let NotImplemented=()=>{
  return (
    <>
      <h1>Esta pagína no esta disponible</h1>
      <Link to="/">Ir al inicio</Link>
    </>
  )
};

let RecolectorOutlet = ()=>{
  return (
    <>
      <h1>Recolector</h1>
      <Outlet/>
    </>
  )
};

let RecolectorEdit =()=>{
  let {id} = useParams();

  return <h1>{id}</h1>
};

let Error404 =()=>{
  return (
    <>
      <Link to="/">Ir al inicio</Link>
      <h1>Esta pagina no existe - 404</h1>
    </>
  )
};

function App() {
  return (
    <BrowserRouter>
      <Provider store={store}>
        <Routes>
          <Route path='/' element={<Hello/>} />

          <Route path='recolector' element={<RecolectorOutlet/>}>
            <Route path='add' element={<SignIn/>} />
            <Route path='edit/:id' element={<RecolectorEdit/>} />
            <Route path='delete' element={<NotImplemented/>} />
          </Route>

          <Route path='*' element={<Error404/>} />
          
        </Routes>
      </Provider>
    </BrowserRouter>
  );
}

export default App;
