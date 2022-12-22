import { createContext, ReactNode, useReducer, useState } from "react";

type HeaderAction = {
  text: string;
  onClick: () => void;
};

type HeaderContextState = {
  visible: boolean;
  title: string;
  showBack: boolean;
  backTitle: string;
  action?: HeaderAction;
};
export type HeaderContextValue = HeaderContextState & {
  update: (update: Partial<HeaderContextState>) => void;
};

const defaultValue = {
  visible: true,
  title: "Header",
  showBack: false,
  backTitle: "",
  update: () => undefined,
};

export const HeaderContext = createContext<HeaderContextValue>(defaultValue);

export function HeaderContextProvider({
  children,
}: {
  children: ReactNode | ReactNode[];
}) {
  const [state, dispatch] = useReducer(
    (_: any, e: any) => ({ ...defaultValue, ...e }),
    {
      visible: true,
      title: "Header",
      showBack: false,
      backTitle: "",
    }
  );

  return (
    <HeaderContext.Provider value={{ ...state, update: dispatch }}>
      {children}
    </HeaderContext.Provider>
  );
}
