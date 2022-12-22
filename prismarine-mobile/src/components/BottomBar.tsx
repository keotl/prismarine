import styles from "./BottomBar.module.css";
import { TabButton } from "./TabButton";

export function BottomBar() {
  return (
    <div className={styles.container}>
      <TabButton icon="album" title="Albums" tabPath="/albums" />
      <TabButton icon="settings" title="Settings" tabPath="/settings" />
    </div>
  );
}
