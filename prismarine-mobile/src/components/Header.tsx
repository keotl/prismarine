import { useContext } from "react";
import { HeaderContext } from "../context/HeaderContext";
import { ActionButton } from "./ActionButton";
import styles from "./Header.module.css";

export function Header() {
  const context = useContext(HeaderContext);
  if (!context.visible) {
    return <></>;
  }
  return (
    <div className={styles.header}>
      <div className={styles.back}>
        {context.showBack && (
          <div onClick={() => window.history.back()}>
            <span className={"material-symbols-rounded"}>arrow_back_ios</span>
          </div>
        )}
      </div>
      <div className={styles.title}>{context.title}</div>
      <div className={styles.action} onClick={context.action?.onClick}>
        {context.action && <div>{context.action.text}</div>}
      </div>
    </div>
  );
}
