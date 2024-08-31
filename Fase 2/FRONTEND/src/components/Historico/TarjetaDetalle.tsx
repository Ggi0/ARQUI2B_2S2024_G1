import React, { useState } from "react";
import { Dialog } from 'primereact/dialog';

export const TarjetaDetalle = ({visible, setVisible, titulo, children}) => {
  return (
    <>
    <Dialog header={titulo}  visible={visible} style={{ width: '50vw' }} onHide={() => {if (!visible) return; setVisible(false); }}>
        {children}
    </Dialog>
    </>
  )
}
