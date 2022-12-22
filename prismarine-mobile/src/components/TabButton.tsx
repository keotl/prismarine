import { useLocation, useNavigate } from "react-router-dom";
import styles from "./TabButton.module.css";
type Props = {
  icon: string;
  title: string;
  tabPath: string;
};

export function TabButton(props: Props) {
  const navigate = useNavigate();
  const location = useLocation();
  const isActive = location.pathname.startsWith(props.tabPath);
  return (
    <div
      className={styles.container + " " + (isActive ? styles.active : "")}
      onClick={() => navigate(props.tabPath + location.search)}
    >
      <span className="material-symbols-rounded">{props.icon}</span>
      <div className={styles.title}>{props.title}</div>
    </div>
  );
}
