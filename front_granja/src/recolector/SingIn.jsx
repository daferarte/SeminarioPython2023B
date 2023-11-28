import React from "react";
import { useDispatch, useSelector } from 'react-redux';

import { logOut, signIn, signUp } from "../store/recolector";

let SignIn = (props) =>{
    let dispatch = useDispatch();
    let recolector = useSelector(state => state.name.name);
    console.log(recolector);

    let doSignIn = () =>{
        dispatch(
            signUp({
                
                    "cedula": "556",
                    "nombres": "pepito",
                    "apellido": "Arteaga",
                    "direccion": "Calle 15 # 4 - 91",
                    "fNacimiento": "2023-11-18",
                    "telefono": "3016889827",
                
            })
        )
    }

    let doLogOut = () =>{
        dispatch(
            logOut()
        )
    }

    return (
        <div>
            {recolector ? <button onClick={doLogOut}>Cerrar sesion</button>:<button onClick={doSignIn}>iniciar sesion</button>}
        </div>
    )
}

export default SignIn;