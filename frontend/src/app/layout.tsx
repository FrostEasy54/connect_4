import type { Metadata } from "next";
import { Inter } from "next/font/google";
import "./globals.css";
import ThemeButton from "@/components/theme-button";
import ThemeProviderWrapper from "./providers";

const inter = Inter({ subsets: ["latin"] });

export const metadata: Metadata = {
  title: "Connect 4",
  description: "Connect 4 game project",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className="h-full">
      <body className={'${inter.className} h-full'}>
        <ThemeProviderWrapper>
          <div className="h-full bg-slate-200 dark:bg-slate-900">
            <ThemeButton />
            {children}
          </div>
        </ThemeProviderWrapper>
      </body>
    </html>
  );
}
