import { useContext, useEffect } from 'react';
import { HeaderContext } from './context/HeaderContext';
import styles from './Logo.module.css'

export function Logo() {
    const header = useContext(HeaderContext);
    useEffect(() => {
	header.update({visible: false})
    }, [header.update]);
    
  return (
      <div className={styles.container}>
      <span className={"material-symbols-rounded " + styles.icon}>music_note</span>
    </div>
  );
}
