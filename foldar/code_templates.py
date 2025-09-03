
NAVBAR_CODE = """\

import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="w-full bg-white dark:bg-gray-900 shadow-md">
      <div className="max-w-7xl mx-auto px-4 py-3 flex items-center justify-between">
        {/* Left */}
        <div className="left flex items-center space-x-4">
          <Link href="/" className="text-xl font-bold text-gray-800 dark:text-gray-100">
            MyLogo
          </Link>
        </div>

        {/* Middle */}
        <div className="middle hidden md:flex space-x-6">
          <Link href="/about" className="text-gray-700 dark:text-gray-200 hover:text-blue-600">
            About
          </Link>
          <Link href="/services" className="text-gray-700 dark:text-gray-200 hover:text-blue-600">
            Services
          </Link>
          <Link href="/pricing" className="text-gray-700 dark:text-gray-200 hover:text-blue-600">
            Pricing
          </Link>
          <Link href="/contact" className="text-gray-700 dark:text-gray-200 hover:text-blue-600">
            Contact
          </Link>
        </div>

        {/* Right */}
        <div className="right flex items-center space-x-3">
          <Link
            href="/login"
            className="px-4 py-2 text-sm font-medium rounded-lg bg-gray-200 dark:bg-gray-700 text-gray-900 dark:text-gray-100 hover:bg-gray-300 dark:hover:bg-gray-600"
          >
            Login
          </Link>
          <Link
            href="/signup"
            className="px-4 py-2 text-sm font-medium rounded-lg bg-blue-600 text-white hover:bg-blue-700"
          >
            Sign Up
          </Link>
        </div>
      </div>
    </nav>
  );
}
"""
BUTTON_CODE = """\
import { ButtonProps } from "@/app/types/uiTypes";

export default function Button({
  content,
  icon,
  onClick,
  className,
}: ButtonProps) {
  return (
    <button
      onClick={onClick}
      className={`px-4 py-2 rounded-2xl font-medium  text-white border-2  transition duration-300 flex items-center gap-3 bg-neutral-500/40 backdrop-blur-lg ${className}`}
    >
      {icon ? icon : ""}
      {content}
    </button>
  );
}

"""

THEME_PROVIDER = """\
"use client";

import * as React from "react";
import { ThemeProvider as NextThemesProvider } from "next-themes";

export function ThemeProvider({
  children,
  ...props
}: React.ComponentProps<typeof NextThemesProvider>) {
  return <NextThemesProvider {...props}>{children}</NextThemesProvider>;
}
"""
THEME_SWITCHER = """\
"use client";

import { Moon, Sun } from "lucide-react";
import { useTheme } from "next-themes";
import { useEffect, useState } from "react";

export const ThemeSwitcher = () => {
  const { theme, setTheme } = useTheme();
  const [mounted, setMounted] = useState(false);

  useEffect(() => {
    setMounted(true);
  }, []);

  if (!mounted) {
    return null;
  }

  return (
    <div className=" flex gap-6">
      <button onClick={() => setTheme(theme === "light" ? "dark" : "light")}>
        {theme === "light" ? (
          <Sun onClick={() => setTheme("dark")} className="" />
        ) : (
          <Moon onClick={() => setTheme("light")} className="" />
        )}
      </button>
    </div>
  );
};
"""

TYPES_CODE = """\
import { ReactNode } from "react";

export interface ButtonProps {
  content: string;
  icon?: ReactNode;
  className?: string;
  onClick?: () => void;
}
"""

HERO_CODE = """\
export default function Hero(){
    return "HELLO World"
}
"""
APP_PAGE_CODE = """\
import Navbar from "./components/includes/Navbar";

export default function Home() {
  return <Navbar />;
}
"""
