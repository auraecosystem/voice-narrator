import subprocess
import os
import sys

def main():
    print("🤖 Initializing JXF Pipeline Orchestration...")
     
    # Get current directory path context
    current_dir = os.path.dirname(os.path.realpath(__file__))
    
    # List of scripts to run sequentially
    scripts = ["generator.py", "dna_generator.py"]
    
    for script in scripts:
        script_path = os.path.join(current_dir, script)
        if os.path.exists(script_path):
            print(f"-> Executing math engine: {script}...")
            # Run child process using current Python interpreter execution layer
            result = subprocess.run([sys.executable, script_path], capture_output=True, text=True)
            if result.returncode == 0:
                print(result.stdout.strip())
            else:
                print(f"❌ Error in execution of {script}:\n{result.stderr}")
        else:
            print(f"❌ Missing file: {script}")

    print("\n🎉 JXF Binary Cache Fully Built. Ready to stream data inside Max/MSP!")

if __name__ == "__main__":
    main()
