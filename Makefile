

clean-pyc:
		find . -name '*.pyc' -exec rm -f {} +

clean-logs:
		find . -name '*.log' -exec rm -f {} +

clean: clean-pyc clean-logs

run:
		python main.py 
