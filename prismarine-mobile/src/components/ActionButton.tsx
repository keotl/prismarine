import styles from "./ActionButton.module.css";

type Props = {
  icon: string;
  onClick?: () => void;
  active?: boolean;
  color?: string;
};

export function ActionButton(props: Props) {
  return (
    <div
      onClick={(e) => {
        if (props.onClick) {
          props.onClick();
        }
        e.stopPropagation();
      }}
    >
      <span
        className={
          "material-symbols-rounded " +
          styles.actionButton +
          (props.active ? " " + styles.active : "")
        }
        style={props.color ? { color: props.color } : undefined}
      >
        {props.icon}
      </span>
    </div>
  );
}
