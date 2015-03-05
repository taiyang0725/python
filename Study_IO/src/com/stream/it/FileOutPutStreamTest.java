package com.stream.it;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileOutputStream;
import java.io.FileWriter;
import java.io.IOException;

public class FileOutPutStreamTest {
	String path = "C:\\Users\\user.MICROSO-02V570Q.000\\Desktop\\小工具\\Linux常用命令大全.txt";
	String path1 = "C:\\Users\\user.MICROSO-02V570Q.000\\Desktop\\小工具\\π.txt";
	String path2 = "C:\\Users\\user.MICROSO-02V570Q.000\\Desktop\\小工具\\π_new.doc";

	private int hasRead;

	public static void main(String[] args) {
		//new FileOutPutStreamTest().output();
		new FileOutPutStreamTest().writeData();
		System.out.println("Great Wall");
	}

	/**
	 * 输出字节流
	 * */
	private void output() {

		FileInputStream inputStream = null;// 输入流
		FileOutputStream outputStream = null;// 输出流

		try {
			inputStream = new FileInputStream(path1);// 创建字节输入流
			outputStream = new FileOutputStream(path2);// 创建字节输出流

			byte[] b = new byte[32];

			// 循环从输入流中取出数据
			while ((hasRead = inputStream.read(b)) > 0) {

				// 每读一次，及写入文件输出流，边读边写
				outputStream.write(b, 0, hasRead);

			}
		} catch (FileNotFoundException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			try {
				if (inputStream != null) {
					inputStream.close();
				}
				if (outputStream != null) {
					outputStream.close();
				}
			} catch (IOException e) {
				// TODO Auto-generated catch block
				e.printStackTrace();
			}
		}

	}

	/**
	 * 输出字符流
	 * */

	private void writeData() {
		FileWriter writer = null;

		try {
			writer = new FileWriter(path2);
			writer.write("        锦瑟-李商隐\r\n");
			writer.write("锦瑟无端五十弦，一弦一柱思华年。\r\n");
			writer.write("庄生晓梦迷蝴蝶，望帝春心托杜鹃。\r\n");
			writer.write("沧海月明珠有泪，蓝田玉暖玉生烟。\r\n");
			writer.write("此情可待成追忆，只是当时已惘然。\r\n");
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		} finally {
			if (writer != null) {
				try {
					writer.close();
				} catch (IOException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
		}

	}

}
